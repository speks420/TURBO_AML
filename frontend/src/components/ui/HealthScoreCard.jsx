import { useState, useEffect } from 'react';
import {
  Box,
  VStack,
  HStack,
  Heading,
  Text,
  Badge,
  Card,
  CardHeader,
  CardBody,
  Grid,
  GridItem,
  Progress,
  Stat,
  StatLabel,
  StatNumber,
  StatHelpText,
  Alert,
  AlertIcon,
  Skeleton,
  SkeletonText,
  useToast,
  Tooltip,
  Divider
} from '@chakra-ui/react';
import { InfoIcon } from '@chakra-ui/icons';
import api from '../../services/api';

/**
 * HealthScoreCard component - displays company health score including taxpayer ratings
 * 
 * @param {string} regNumber - Company registration number
 * @returns {JSX.Element} HealthScoreCard component
 */
const HealthScoreCard = ({ regNumber }) => {
  const [healthData, setHealthData] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const toast = useToast();

  useEffect(() => {
    fetchHealthScore();
  }, [regNumber]);

  const fetchHealthScore = async () => {
    setIsLoading(true);
    setError(null);
    
    try {
      const response = await api.get(`/api/financial/${regNumber}/health-score`);
      setHealthData(response.data);
    } catch (err) {
      console.error('Error fetching health score:', err);
      setError(err.response?.data?.detail || 'Failed to load health score');
      
      // Don't show toast for 404 errors (no financial data)
      if (err.response?.status !== 404) {
        toast({
          title: 'Error loading health score',
          description: err.response?.data?.detail || 'Please try again later',
          status: 'error',
          duration: 5000,
          isClosable: true,
        });
      }
    } finally {
      setIsLoading(false);
    }
  };

  const getScoreColor = (score) => {
    if (score >= 80) return 'green';
    if (score >= 60) return 'yellow';
    if (score >= 40) return 'orange';
    return 'red';
  };

  const getGradeColor = (grade) => {
    if (['A+', 'A', 'A-'].includes(grade)) return 'green';
    if (['B+', 'B', 'B-'].includes(grade)) return 'blue';
    if (['C+', 'C', 'C-'].includes(grade)) return 'yellow';
    if (['D+', 'D', 'D-'].includes(grade)) return 'orange';
    return 'red';
  };

  const getRiskColor = (risk) => {
    switch (risk) {
      case 'LOW': return 'green';
      case 'MEDIUM': return 'yellow';
      case 'HIGH': return 'orange';
      case 'CRITICAL': return 'red';
      default: return 'gray';
    }
  };

  if (isLoading) {
    return (
      <Card>
        <CardHeader>
          <Skeleton height="20px" width="200px" />
        </CardHeader>
        <CardBody>
          <VStack spacing={4}>
            <Skeleton height="80px" width="100%" />
            <SkeletonText noOfLines={3} spacing="4" />
          </VStack>
        </CardBody>
      </Card>
    );
  }

  if (error) {
    return (
      <Alert status="info">
        <AlertIcon />
        <Box>
          <Text fontWeight="bold">Health Score Unavailable</Text>
          <Text fontSize="sm">Insufficient financial data to calculate health score</Text>
        </Box>
      </Alert>
    );
  }

  if (!healthData) {
    return (
      <Alert status="info">
        <AlertIcon />
        <Text>No health score data available for this company.</Text>
      </Alert>
    );
  }

  return (
    <Card>
      <CardHeader>
        <HStack justify="space-between" align="center">
          <Heading size="md" color="purple.600">💚 Company Health Score</Heading>
          <Tooltip label="Based on financial ratios, growth trends, and taxpayer rating">
            <InfoIcon color="gray.400" />
          </Tooltip>
        </HStack>
      </CardHeader>
      <CardBody>
        <VStack spacing={6}>
          {/* Overall Health Score */}
          <Grid templateColumns="repeat(3, 1fr)" gap={6} w="100%">
            <GridItem>
              <Stat textAlign="center">
                <StatLabel>Overall Score</StatLabel>
                <StatNumber fontSize="3xl" color={`${getScoreColor(healthData.health_score)}.500`}>
                  {healthData.health_score}
                </StatNumber>
                <StatHelpText>
                  <Badge colorScheme={getGradeColor(healthData.health_grade)} fontSize="md" p={1}>
                    Grade: {healthData.health_grade}
                  </Badge>
                </StatHelpText>
              </Stat>
            </GridItem>
            <GridItem>
              <Stat textAlign="center">
                <StatLabel>Risk Level</StatLabel>
                <StatNumber fontSize="xl">
                  <Badge colorScheme={getRiskColor(healthData.risk_level)} fontSize="lg" p={2}>
                    {healthData.risk_level}
                  </Badge>
                </StatNumber>
                {healthData.altman_z_score && (
                  <StatHelpText>
                    Z-Score: {healthData.altman_z_score}
                  </StatHelpText>
                )}
              </Stat>
            </GridItem>
            <GridItem>
              <Stat textAlign="center">
                <StatLabel>Years Analyzed</StatLabel>
                <StatNumber fontSize="2xl" color="blue.500">
                  {healthData.years_analyzed}
                </StatNumber>
                <StatHelpText>
                  {healthData.trend_direction && (
                    <Badge colorScheme="blue" variant="outline">
                      {healthData.trend_direction}
                    </Badge>
                  )}
                </StatHelpText>
              </Stat>
            </GridItem>
          </Grid>

          <Divider />

          {/* Component Scores */}
          <Box w="100%">
            <Heading size="sm" mb={4} color="gray.600">Score Breakdown</Heading>
            <Grid templateColumns="repeat(2, 1fr)" gap={4}>
              {[
                { label: 'Liquidity', score: healthData.liquidity_score, weight: '20%' },
                { label: 'Profitability', score: healthData.profitability_score, weight: '25%' },
                { label: 'Solvency', score: healthData.solvency_score, weight: '15%' },
                { label: 'Efficiency', score: healthData.efficiency_score, weight: '15%' },
                { label: 'Growth', score: healthData.growth_score, weight: '10%' },
                { label: 'Taxpayer Rating', score: healthData.taxpayer_rating_score, weight: '15%' }
              ].map((component) => (
                <GridItem key={component.label}>
                  <VStack align="start" spacing={2}>
                    <HStack justify="space-between" w="100%">
                      <Text fontSize="sm" fontWeight="medium">{component.label}</Text>
                      <HStack spacing={2}>
                        <Text fontSize="sm" color="gray.500">({component.weight})</Text>
                        <Text fontSize="sm" fontWeight="bold">
                          {component.score ? Math.round(component.score) : 'N/A'}
                        </Text>
                      </HStack>
                    </HStack>
                    <Progress 
                      value={component.score || 0} 
                      size="sm" 
                      colorScheme={getScoreColor(component.score || 0)}
                      w="100%"
                    />
                  </VStack>
                </GridItem>
              ))}
            </Grid>
          </Box>

          {/* Strengths and Weaknesses */}
          <Grid templateColumns="repeat(2, 1fr)" gap={6} w="100%">
            {healthData.strengths && healthData.strengths.length > 0 && (
              <GridItem>
                <VStack align="start" spacing={2}>
                  <Heading size="sm" color="green.600">💪 Strengths</Heading>
                  {healthData.strengths.map((strength, index) => (
                    <Text key={index} fontSize="sm" color="green.700">
                      • {strength}
                    </Text>
                  ))}
                </VStack>
              </GridItem>
            )}
            
            {healthData.weaknesses && healthData.weaknesses.length > 0 && (
              <GridItem>
                <VStack align="start" spacing={2}>
                  <Heading size="sm" color="red.600">⚠️ Areas for Improvement</Heading>
                  {healthData.weaknesses.map((weakness, index) => (
                    <Text key={index} fontSize="sm" color="red.700">
                      • {weakness}
                    </Text>
                  ))}
                </VStack>
              </GridItem>
            )}
          </Grid>

          {/* Recommendations */}
          {healthData.recommendations && healthData.recommendations.length > 0 && (
            <Box w="100%">
              <Heading size="sm" mb={3} color="blue.600">💡 Recommendations</Heading>
              <VStack align="start" spacing={1}>
                {healthData.recommendations.map((recommendation, index) => (
                  <Text key={index} fontSize="sm" color="blue.700">
                    • {recommendation}
                  </Text>
                ))}
              </VStack>
            </Box>
          )}
        </VStack>
      </CardBody>
    </Card>
  );
};

export default HealthScoreCard; 